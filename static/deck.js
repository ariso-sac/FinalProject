function Delete(id) {
    fetch("/api/deck" + "/" + id, {
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
function savedata(id) {
    var x = document.getElementById(id).value;
    if (x==''){
        alert("Enter Name");
    }
    else{
    var data = { "name": x }
    console.log(JSON.stringify(data))
    fetch("/api/deck" + "/" + id, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(() => {
        alert("Updated")
    }).catch(err => {
        alert(Error);
        console.error(err);
    })
    location.reload()
}}