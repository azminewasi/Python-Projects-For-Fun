#include <stdio.h> 
#include <string.h>
int main ()
{
  char d[100];
  int b,i,f,no;
  float a;

  scanf ("%d",&no);

  a = (no/2)+0.5;
  b = a;

  for (i=0;i<=b;i++)
  {
    d[i]= '*';

    d[i+1]= '\0';
    printf ("%s\n",d);
  }

  for (i=0;i<b;i++)
  {
    d[i]= 0;

    d[i+1]= '\0';
  }
  //
  //f = b;
  b = b-1;
  for (i=0;i<b;i++)
  {
    d[i]= '*';

    d[i+1]= '\0';
    // printf ("%s\n",d);
  }
  for (i=b;i>=0;i--)
  {
    printf ("%s\n",d);
    d[i] = '\0';
  }
}