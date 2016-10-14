#include "ghttp.h"
#include "stdio.h"
#include "unistd.h"

int isFileExist(char * savePath) {  
    if (!access(savePath, F_OK)) {  
        return 1;  
    } else {  
        return 0;  
    }  
}
 
int download(char *uri, char *savePath) {          
    if(!isFileExist(savePath))  
    {  
        printf("savePath not exist ");  
        return -1;  
    } 	
    
    ghttp_request *request = ghttp_request_new();  
	
    if (ghttp_set_uri(request, uri) == -1)  
        return -1;  
	
	ghttp_set_header(request, http_hdr_Connection, "close");
	
    if (ghttp_set_type(request, ghttp_type_get) == -1)//get  
        return -1; 
	
    ghttp_prepare(request);  
    ghttp_status status = ghttp_process(request);  
    if (status == ghttp_error)  
        return -1;  
	
    char* buf = ghttp_get_body(request);  
    int bytes_read = ghttp_get_body_len(request); 
	
	FILE * pFile = fopen(savePath, "wb");  
    fwrite(buf, 1, strlen(buf), pFile);  
    fclose(pFile);  
	
	ghttp_request_destroy(request);
    return 0;  
}

char* request(char *url)
{
	ghttp_request *request = ghttp_request_new(); 		
	
    if (ghttp_set_uri(request, url) == -1)  
        return NULL; 
	
	ghttp_set_header(request, http_hdr_Connection, "close");
	
    if (ghttp_set_type(request, ghttp_type_get) == -1)//get  
        return NULL; 
	
    ghttp_prepare(request);  
    ghttp_status status = ghttp_process(request);  
    if (status == ghttp_error)  
        return NULL;  
	
    char* buf = ghttp_get_body(request);  
    int bytes_read = ghttp_get_body_len(request); 
	
	char* ret = malloc(bytes_read+1);
	memcpy(ret, buf, bytes_read);
	ret[bytes_read] = '\0';
	
	ghttp_request_destroy(request);	
	return ret;
}
 
int main()
{
	char* ret = request("https://cn.bing.com");
	if (ret == NULL)
	{
		printf("NULL");
		return 0;
	}
	printf(ret);
	

	
	return 0;
}

