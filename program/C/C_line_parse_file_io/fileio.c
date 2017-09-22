#include <stdio.h>
#include <time.h>



ssize_t parse_line(FILE *fp,void (*parse_function)(char buff[])) {
	char *line=NULL;
	size_t len=0;
	ssize_t nread;
	if ((nread=getline(&line,&len,fp))<0) {
		free(line);
		return nread;
	};
	parse_function(line);
	free(line);
	return nread;
}


void print_line(char buff[]){
	printf("%s\n",buff);
}



void get_time(char buff[]) {
	char stime[1024],rtype[1024],jobid[1024],jobbody[1024];
	int i,n=0;
	i=get_delimit(buff,n,';',stime,&n);

	i=get_delimit(buff,n,';',rtype,&n);
	const char type_lic[]="L;";
	if (strcmp(type_lic,rtype)==0) {
		return;
	}


	i=get_delimit(buff,n,';',jobid,&n);

	i=get_delimit(buff,n,';',jobbody,&n);

	printf("%s",stime);
	printf("%s",rtype);
	printf("%s",jobid);
	printf("%s",jobbody);
	
	printf("\n");

}

int get_delimit(char* buff,int start,int delimit,char dest[], int* nextloc) {
	int i;
	size_t t=0;
	memset(dest,'\0',1024);
	for(i=start;buff[i]!=delimit;++i,++t) {
		if (buff[i]=='\n') break;
	};

	*nextloc=i+1;
	memcpy(dest,buff+start,t+1);
	return t;
}


int main() {
	FILE *fp;
	fp=fopen("20170209","r");
	int s;
	while ((s=parse_line(fp,&get_time))>0) {
	};
	exit(0);
}
