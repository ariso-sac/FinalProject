function Work() {
    fetch("/api/cardsbydeck/1")
        .then(response => response.json())
        .then(data => document.getElementById('main').innerHTML = data[0].back
        )
}
function show() {
    document.getElementById("Answer").style.visibility = "visible";
}
function main(id) {
    x = document.getElementById('num').innerHTML
    y = parseInt(x)
    i = parseInt(id)
    fetch("/api/cardsbydeck/" + i)
        .then(response => response.json())
        .then(data => {
            l = data.length - 1
            console.log(data)
            if (x < l + 1) {
                document.getElementById('Question').innerHTML = data[y].front
                document.getElementById("Answer").style.visibility = "hidden"
                document.getElementById('Answer').innerHTML = data[y].back
                document.getElementById('num').innerHTML = y + 1
            }
            else {
                document.getElementById('num').innerHTML = 0
                document.getElementById('Question').innerHTML = "Ended"
                document.getElementById('Answer').innerHTML = "Ended"
            }
        })
}
function easy() {
    x = document.getElementById('easy').innerHTML
    x = parseInt(x)
    y = x + 1
    document.getElementById('easy').innerHTML = y
}
function moderate() {
    x = document.getElementById('moderate').innerHTML
    x = parseInt(x)
    y = x + 1
    document.getElementById('moderate').innerHTML = y
}
function hard() {
    x = document.getElementById('hard').innerHTML
    x = parseInt(x)
    y = x + 1
    document.getElementById('hard').innerHTML = y
}
//let response = await fetch('https://8080-cs-975820098487-default.cs-asia-southeast1-yelo.cloudshell.dev/api/user/1/deck/1');
async function score(u, d) {
    user = parseInt(u)
    console.log(d)
    deck = parseInt(d)
    var response = await fetch('/api/user/' + user + '/deck/' + deck);
    console.log(response.status); // 200
    console.log(response.statusText); // OK
    x = document.getElementById('easy').innerHTML
    y = document.getElementById('moderate').innerHTML
    z = document.getElementById('hard').innerHTML
    var data={
        'easy':x,
        'moderate':y,
        'hard':z
    }
    if (response.status==500){
        fetch('/api/user/' + user + '/deck/' + deck, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).then(() => {
            alert("SCORE SAVED")
        }).catch(err => {
            alert(Error);
            console.error(err);
        })
    }
    else{
        fetch('/api/user/' + user + '/deck/' + deck, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).then(() => {
            alert("SCORE SAVED")
        }).catch(err => {
            alert(Error);
            console.error(err);
        })
    }
}
