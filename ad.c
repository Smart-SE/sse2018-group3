/* AD */

#include <stdio.h>

#include <wiringPiSPI.h>
#include <wiringPi.h>


unsigned char outdat[2] = {0xd0,0x00};
 int main(int argc,char *argv[] )
{
	int 	fd,data;
	fd=wiringPiSPISetup(0,1000000);
	if(fd<0){
		printf("SPI Open errer\n");
		return 1;
	}

//	while(1)
//	{
	data = wiringPiSPIDataRW(0,outdat,2);
	printf("Data[%d]\n",data);
	printf("%02XH\n",(0x03&outdat[0]));
	printf("%02XH\n",outdat[1]);
	
	//outdat[0] = 0xd0;
//	}

	return 0;
}
