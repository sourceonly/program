#include <unistd.h>
#include <shadow.h>
#include <pwd.h>
#include <string.h>
#include <malloc.h>

char* get_salt(const char* passwd) ;
int usage() ;
int main(int argc,char** argv) {
	if (argc!=3) {
		usage();
	 	exit(2);
	}
	char* username=argv[1];
	char* passwd=argv[2];
	struct spwd *p=getspnam(username);
	if (p==NULL) {
		printf("username %s not found ", username);
		exit(1); }
	char* crypto_pw=p->sp_pwdp;
	int i=0,d=0;
	char* salt=get_salt(crypto_pw);
		
	printf("salt=%s\n",salt);
	
	char* md=crypt(passwd,salt);
	printf("passwd=%s\n",md);
	if (strcmp(md,crypto_pw)==0) {
		printf("same\n");
	} else {
		printf("not same\n");
		exit(1);
	}
	exit(0);	
}

char* get_salt(const char* passwd) {
	/* get the salt from passwd entry */
	int i,j=0;
	char * salt=malloc(sizeof(char)*strlen(passwd));
	for (i=0;i<strlen(passwd);i++) {
		if (j>=3) {	
			salt[i]='\0';
			break;
		}		
		if (passwd[i]=='$') j++;
		salt[i]=passwd[i];
	}
	return salt;
	
}

int usage() {
	printf("usage: a.out  username passwd\n") ;
	printf("\treturn 0 for the same\n\t1 other wise\n");
}
