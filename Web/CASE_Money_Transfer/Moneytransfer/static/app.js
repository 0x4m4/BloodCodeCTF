async function transfer()
{
    userid = document.getElementById('userid').value;
    amount = document.getElementById('amount').value;
    ct = document.getElementById('csrf_token').value;
    console.log(amount);
    if(userid && amount )
    {
        f = await fetch('/transfer?userid='+userid+'&amount='+amount+'&csrf_token='+ct);
        j = await f.json();
        console.log(j);
        document.getElementById('msg').innerHTML=j.msg;
        document.getElementById('msg').style.fontSize='1rem';
        if(j.stat == 'err')
        {
            document.getElementById('msg').style.color='red';
        }
       else
        {
            document.getElementById('msg').style.color='#005';
        }
        document.getElementById('msg').style.display='block';
        console.log('hi');
    }
}

function submitfeedback()
{
    var feedbackv = document.getElementById('feedta').value;
    data = {feedback:feedbackv}
    document.getElementById('submission').innerHTML='Here\'s what you submitted<br/>'+feedbackv;
    fetch('/feedbacksubmit', 
    {
        method: "POST", 
        
        headers: {
            'Accept': 'application/json',
            "Content-Type": "application/json",
            
        },
        
        body: JSON.stringify(data), 
    }
    )
}