// Initialize Cloud Firestore through Firebase
firebase.initializeApp({
    apiKey: "AIzaSyAGe3PNzHxQqSc4jOEuziv3sAhn3-Pb7HA",
    authDomain: "keiki-pet.firebaseapp.com",
    projectId: "keiki-pet",
  });
  
 var db = firebase.firestore();

function guardar(){
    var nombre =document.getElementById('usuario').value;
    var email =document.getElementById('email').value;
    var contraseña =document.getElementById('contraseña').value;

    console.log("guardado de datos");

    db.collection("users").add({
        first: nombre,
        last: email,
        born: contraseña,
    })
    .then(function(docRef) {
        console.log("Document written with ID: ", docRef.id);
        alert("guardado"+nombre)
    })
    .catch(function(error){
        console.error("Error adding document: ", error);
        alert("error "+nombre)
    });
    alert("finalizar"+nombre)
}
