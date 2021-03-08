window.onload = function()
{
    var Width = screen.availWidth;
    var Height = screen.height;
    if( /Android|webOS|iPhone|iPad|Mac|Macintosh|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    document.documentElement.style.setProperty('--Top',(Height/4).toString()+'px');
    document.documentElement.style.setProperty('--Left',(Width/4.5).toString()+'px');
    document.documentElement.style.setProperty('--TopR',((Height/3)+(Height/23)).toString()+'px');
    document.documentElement.style.setProperty('--LeftR',((Width/2.5)-(Width/1.32)).toString()+'px');
    document.documentElement.style.setProperty('--HR',(30).toString()+'%');
    console.log('Mob');
       }
       else
       {
    document.documentElement.style.setProperty('--Top',(Height/3).toString()+'px');
    document.documentElement.style.setProperty('--Left',(Width/2.5).toString()+'px');
    document.documentElement.style.setProperty('--TopR',((Height/3)+120).toString()+'px');
    document.documentElement.style.setProperty('--LeftR',((Width/2.5)-70).toString()+'px');
    document.documentElement.style.setProperty('--HR',(30.5).toString()+'%');
       }
};