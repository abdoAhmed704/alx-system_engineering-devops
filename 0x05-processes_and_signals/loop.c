#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>


void handler(int num) {
	write(STDOUT_FILENO, "I won't die\n",13);
}

int main(void)
{
	int i = 1;
	signal(SIGINT, handler);	

	while(i)
	{
		printf("%i\n", i);
		i++;
		sleep(1);
	}
}
