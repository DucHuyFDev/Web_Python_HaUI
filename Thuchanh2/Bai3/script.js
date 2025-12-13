cnt_guess = 0, result = 0;

document.addEventListener("DOMContentLoaded", () => {
    cnt_guess = 0;
    result = Math.floor(Math.random() * 100);
})

document.querySelector("#guess_btn").addEventListener("click", () => {
    let guess = document.getElementById("guess").value;
    if (guess < 0 || guess > 100){
        document.querySelector("#congrat").innerHTML = "Số trong đoạn 1 đến 100 !";
    }
    
    else if (result > guess){
        document.querySelector("#congrat").innerHTML = "Cao hơn !";
        cnt_guess++;
    }
    else if (result < guess){
        document.querySelector("#congrat").innerHTML = "Thấp hơn !";
        cnt_guess++;
    }
    else{
        document.querySelector("#congrat").innerHTML = `
            Chính xác !!! Chúc mừng bạn đã đoán đúng sau ${cnt_guess} lần !
        `;
    }
})

document.getElementById("replay").addEventListener("click", () => {
    cnt_guess = 0;
    result = Math.floor(Math.random() * 100);
    document.querySelector("#congrat").innerHTML = "";
    document.querySelector("#guess").value = "";
})