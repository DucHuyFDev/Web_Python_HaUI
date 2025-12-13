list_task = ["Công việc 1", "Công việc 2"]

document.getElementById("them").addEventListener("click", () => {
    let new_task = document.getElementById("addtask").value;
    if (!new_task){
        return;
    }
    list_task.push(new_task);
    document.getElementById("addtask").value = "";
    render();
})

document.addEventListener("DOMContentLoaded", () => {
  render();
});

function xoa(index){
    list_task.splice(index,1);
    render();
}


function render(){
    let ul_html = document.getElementById("list_task");
    ul_html.innerHTML = "";
    list_task.forEach((value, index) =>{
        ul_html.innerHTML += `
            <li>
                ${value}
                <button id="xoa" onclick="xoa(${index})">Xóa</button>
            </li>
        `
    });
}