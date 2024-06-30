#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
void get_flag(){
  char c;
  int fp = open("/flag", O_RDONLY);
  printf("Bohat teez ho rhe ho, discord per send kerna solution: ");
  while ( read(fp, &c, 1) > 0 )
    fprintf(stdout, "%c", c);
  close(fp);
}

void printBanner() {
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
}

int main(void){
    printBanner();
    char user_input[6]; 
    char pass[28] = "SSCIT{f4ke_fl4g_f0r_t3st1ng}";
    read(0, user_input, 7);
    strcmp(user_input, pass) == 0 ? get_flag() :printf("Error");
    return 0;
}
