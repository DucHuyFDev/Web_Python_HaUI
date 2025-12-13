// onblur: kích hoạt khi mất focus
// onkeydown: khi nhả phím nào đó ra khỏi bàn phím (gõ xong 1 phím)

// Kích hoạt đổi màu nền và focus
const inputs = document.querySelectorAll("#name, #email, #pass, #repass");
const err = document.getElementById("err")
inputs.forEach(inp => {
    inp.addEventListener("focus", () => {
        inp.style.backgroundColor = "#c4d4ed";
    });

    inp.addEventListener("blur", () => {
        inp.style.backgroundColor = "#ffffff";
    });
});

inputs.forEach(inp => {
    inp.addEventListener("keyup", () => {
        if (inp.value === "") {
            err.innerHTML = `${inp.id} đang trống`;
        }
        else{
            if (inp.id ==='repass'){
                const pass = inputs[2].value;
                if (inp.value !== pass){
                    err.innerHTML = `Mật khẩu xác nhận không trùng khớp`;
                    return;
                }
            }
            err.innerHTML = ''
        }
    });
});



