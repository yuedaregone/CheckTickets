<?
require "select_city.php";
class funmgr
{
	public function get_result_by_cmd($cmd)
	{
		if($cmd == "?" || $cmd == "？")
        {
        	return $this->help();
        }
        else if($cmd == "天气")
        {
            return $this->weather();
        }
        else if($cmd == "火车票")
        {
            return $this->ticket_tips();
        }
        else if(strpos($cmd, "1#") !== FALSE)
        {
            list($index,$time,$from,$to) = split("#", $cmd, 4);
            return $this->tickets($time,$from,$to);
        }
        else
        {
            $string = "你好啊！";
            return $string;
        }
	}

	private function help()
	{
		return date("Y-m-d H:i:s",time());
	}

	private function weather()
	{
		$url='http://apis.haoservice.com/weather?cityname=上海&key=19209e21fb0a4488a0b78d1bc3c3957c';
		$html = file_get_contents($url);
		$json_obj = json_decode($html);

        $url1='http://apis.haoservice.com/air/cityair?city=上海&key=b7f648f1bd6142e4932609f967f85c7e';
		$html1 = file_get_contents($url1);
		$json_obj1 = json_decode($html1);

        if ($json_obj->error_code == 0)
        {
            $weatherInfo = $json_obj->result;
            $weatherToday = $weatherInfo->today;

            $air_string = "";
            if ($json_obj1->error_code == 0)
            {
                $airInfo = $json_obj1->result;
                $str = "空气质量：%s \nPM2.5：%s";
                $air_string = sprintf($str, $airInfo->Quality,substr($airInfo->PM25,0,strlen($airInfo->PM25) - 10));
            }

            $string = $weatherToday->city." ".$weatherToday->weather." ".$weatherToday->temperature."\n".$weatherToday->wind."\n"."当前温度:".$weatherInfo->sk->temp."\n".$air_string."\n".$weatherToday->dressing_advice;
        	return $string;
        }
        return "Hello World!";
	}
    
    private function ticket_tips()
    {
        return "请发送：1#时间#出发地#目的地\n例如：1#2015-12-30#上海#鲁山";
    }

	private function tickets($time,$from,$to)
	{
        $from_station = "SHH";
        $to_station = "ZZF";
        $temp_str = $this->decode_city($from);
        if ($temp_str !== FALSE)
        {
            $from_station = $temp_str;
        }
        $temp_str = $this->decode_city($to);
        if ($temp_str !== FALSE)
        {
            $to_station = $temp_str;
        }
        
        
        $url='https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='.$time.'&from_station='.$from_station.'&to_station='.$to_station;
        $html = file_get_contents($url);
        $json_obj = json_decode($html);
        if($json_obj->httpstatus == 200)
        {
            $tickets_info = "";//"时间:".str_replace("&nbsp;", " ",$json_obj->data->searchDate)."\n\n";
            $data_array = $json_obj->data->datas;
            $data_count = count($data_array);
			
            if ($data_count > 0)
            {
                for ($i=0; $i < $data_count; $i++) {
                    $ticket_data = $data_array[$i];
                    $info_out = "车次:".$ticket_data->station_train_code."\n";
                    $info_out = $info_out.$ticket_data->from_station_name." --- ".$ticket_data->to_station_name."\n";
                    $info_out = $info_out."时间:".$ticket_data->start_time." --- ".$ticket_data->arrive_time."\n";
                    $info_out = $info_out."一等座:".$ticket_data->zy_num." 二等座:".$ticket_data->ze_num." 硬卧:".$ticket_data->yw_num." 硬座".$ticket_data->yz_num."\n";
    
                    $tickets_info = $tickets_info.$info_out."\n";
                }
                return $tickets_info;
            }
            else
            {
                return "查找不到信息！";
            }            
        }
        return "error:".$json_obj->httpstatus;
	}    
    
    private function decode_city($city)
    {
        if ($city == "上海")
        {
            return "SHH";
        }
        else if ($city == "郑州")
        {
            return "ZZF";
        }
        else if ($city == "鲁山")
        {
            return "LAF";
        }        
        return get_city_code($city);
    }
}
?>
