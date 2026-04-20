<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<script src="https://telegram.org/js/telegram-web-app.js"></script>
</head>

<body style="text-align:center; font-family:sans-serif; background:#111; color:white;">

<h2>📊 ระบบบันทึกเวลา</h2>

<h1 id="timer">00:00</h1>

<button onclick="start('toilet')" style="width:90%;padding:20px;">🚻 เริ่มเข้าห้องน้ำ</button><br><br>
<button onclick="start('smoke')" style="width:90%;padding:20px;">🚬 เริ่มสูบบุหรี่</button><br><br>
<button onclick="stop()" style="width:90%;padding:20px;background:red;color:white;">⛔ หยุด</button>

<audio id="alarm">
<source src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg">
</audio>

<script>
let startTime=null, interval=null, alerted=false, type=null;

function start(t){
 if(startTime){alert("เริ่มแล้ว");return;}
 startTime=new Date(); type=t; alerted=false;

 interval=setInterval(()=>{
   let diff=Math.floor((new Date()-startTime)/1000);
   let m=String(Math.floor(diff/60)).padStart(2,'0');
   let s=String(diff%60).padStart(2,'0');
   document.getElementById("timer").innerText=m+":"+s;

   if(diff>=600 && !alerted){
     document.getElementById("alarm").play();
     alerted=true;
   }
 },1000);

 Telegram.WebApp.sendData(JSON.stringify({action:"start",type:t,time:new Date()}));
}

function stop(){
 if(!startTime){alert("ยังไม่เริ่ม");return;}
 clearInterval(interval);

 Telegram.WebApp.sendData(JSON.stringify({action:"stop",type:type,time:new Date()}));

 startTime=null;
 document.getElementById("timer").innerText="00:00";
}
</script>

</body>
</html>
