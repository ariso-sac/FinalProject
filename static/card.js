function Crt() {
    var x = document.getElementById("front").value;
    var y = document.getElementById("back").value;
    var z = document.getElementById("deck_id").value;
    if (x==''||y==''||z==''){
        alert("Wrong Inputs")
    }
    else{
    var data = {
        "front": x,
        "back": y,
        "deck": z
    }
    console.log(JSON.stringify(data))
    fetch("/api/card", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(() => {
        alert("Created")
    }).catch(err => {
        alert(Error);
        console.error(err);
    })
    window.location.replace("/");
}}
function Delete(id) {
    fetch("/api/card" + "/" + id, {
        method: 'DELETE'
    }).then(() => {
        alert("Removed");
        console.log('removed');
    }).catch(err => {
        alert("Error");
        console.error(err);
    });
    location.reload()
}