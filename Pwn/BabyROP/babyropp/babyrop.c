#include <stdio.h>

void banner(){
    printf("                                                                           \n");
    printf(" ██▀███   ▒█████   ▒█████  ▄▄▄█████▓▒██   ██▒ ██▀███   ▄▄▄       ███▄    █ \n");
    printf("▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒▓  ██▒ ▓▒▒▒ █ █ ▒░▓██ ▒ ██▒▒████▄     ██ ▀█   █ \n");
    printf("▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒▒ ▓██░ ▒░░░  █   ░▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒\n");
    printf("▒██▀▀█▄  ▒██   ██░▒██   ██░░ ▓██▓ ░  ░ █ █ ▒ ▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒\n");
    printf("░██▓ ▒██▒░ ████▓▒░░ ████▓▒░  ▒██▒ ░ ▒██▒ ▒██▒░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░\n");
    printf("░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░   ▒ ░░   ▒▒ ░ ░▓ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ \n");
    printf("  ░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░     ░    ░░   ░▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░\n");
    printf("  ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒    ░       ░    ░    ░░   ░   ░   ▒      ░   ░ ░ \n");
    printf("   ░         ░ ░      ░ ░            ░    ░     ░           ░  ░         ░ \n");
    printf("                                                                           \n");
    printf("Do something like monkeys: ");
    fflush(stdout);
}
char bin_sh[] = "/bin/sh\x00";
void gadgets(){
  asm("pop %rdi; ret");
}
void hitme(int param){
    system(param);
}

int main(){
  
  char buffer[2100];
  banner();
  gets(buffer);
  return 0;
}