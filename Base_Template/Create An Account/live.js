const submit = document.getElementById('submit');

submit.addEventListener('click', function(event){
    event.preventDefault();
    const email = document.getElementById('email').value;
    const fName = document.getElementById('f-name').value;
    const lName = document.getElementById('l-name').value;
    const password = document.getElementById('password').value;
    if (fName == ""){
        const fErr = document.getElementById('f-err');
        document.getElementById('f-name').style.border = "1px solid hsl(0, 100%, 74%)"
        document.getElementById('f-name').style.backgroundImage = "url('./images/alert.png')"
        document.getElementById('f-name').style.backgroundPosition = "center right"
        document.getElementById('f-name').style.backgroundRepeat = "no-repeat"
        document.getElementById('f-name').style.backgroundSize = "7% auto"
        fErr.innerText = "First Name cannot be empty";
    }
    if (lName == ""){
        const lErr = document.getElementById('l-err');
        document.getElementById('l-name').style.border = "1px solid hsl(0, 100%, 74%)"
        document.getElementById('l-name').style.backgroundImage = "url('./images/alert.png')"
        document.getElementById('l-name').style.backgroundPosition = "center right"
        document.getElementById('l-name').style.backgroundRepeat = "no-repeat"
        document.getElementById('l-name').style.backgroundSize = "7% auto"
        lErr.innerText = "Last Name cannot be empty";
    }
    if (email == ""){
        const eErr = document.getElementById('email-err');
        document.getElementById('email').style.border = "1px solid hsl(0, 100%, 74%)"
        document.getElementById('email').style.backgroundImage = "url('./images/alert.png')"
        document.getElementById('email').style.backgroundPosition = "center right"
        document.getElementById('email').style.backgroundRepeat = "no-repeat"
        document.getElementById('email').style.backgroundSize = "7% auto"
        eErr.innerText = "Email cannot be empty";
    }
    if (email != ""){
        const mailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if (email.match(mailFormat)){
                return (true)
            }
            const eErr = document.getElementById('email-err');
            eErr.innerText = "Looks like this is not an email";
            document.getElementById('email').style.border = "1px solid hsl(0, 100%, 74%)"
            document.getElementById('email').style.backgroundImage = "url('./images/alert.png')"
            document.getElementById('email').style.backgroundPosition = "center right"
            document.getElementById('email').style.backgroundRepeat = "no-repeat"
            document.getElementById('email').style.backgroundSize = "7% auto"
    }
    if (password == ""){
        const pErr = document.getElementById('p-err');
        document.getElementById('password').style.border = "1px solid hsl(0, 100%, 74%)"
        document.getElementById('password').style.backgroundImage = "url('./images/alert.png')"
        document.getElementById('password').style.backgroundPosition = "center right"
        document.getElementById('password').style.backgroundRepeat = "no-repeat"
        document.getElementById('password').style.backgroundSize = "7% auto"
        pErr.innerText = "Password cannot be empty";
    }
});