
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 

void error(const char *msg)
{
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, n;
    struct sockaddr_in serv_addr;
    struct hostent *server;
	
    char buffer[256];
	char * info="POST /RPC2 HTTP/1.0\nContent-Type: application/xml\nContent-Length: %d\n\n%s\n";
	char * xmlbody="<?xml version=\'1.0\'?><methodCall><methodName>run_command1</methodName><params><param><value><string>ls -ltr</string></value></param></params></methodCall>";
	char * infobody=malloc((strlen(info)+strlen(xmlbody)+10)*sizeof(char));
	bzero(infobody,strlen(infobody)+1);
    portno = 8000;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) 
        error("ERROR opening socket");
    server = gethostbyname("localhost");
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, 
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);
    serv_addr.sin_port = htons(portno);
    if (connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0) 
        error("ERROR connecting");
    printf("Please enter the message: \n");
    bzero(buffer,256);
    /* fgets(buffer,255,stdin); */

	sprintf(infobody,info,strlen(xmlbody),xmlbody);
	printf("%s\n",infobody);
	n = write(sockfd,infobody,strlen(infobody));
	printf("%d\n",n);

    if (n < 0) 
         error("ERROR writing to socket");
    bzero(buffer,256);
	n=1;
	while (n>0) {
	  n=read(sockfd,buffer,255);
	  printf("%s",buffer);
	  bzero(buffer,255);
	}
    close(sockfd);
    return 0;
}
