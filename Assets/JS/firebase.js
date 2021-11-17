  const firebaseConfig = {
    apiKey: "AIzaSyDzTu0mU0MvkvCbsOEfJ0BPnFGaJuFTCpQ",
    authDomain: "pag-keikipet.firebaseapp.com",
    projectId: "pag-keikipet",
    storageBucket: "pag-keikipet.appspot.com",
    messagingSenderId: "577523729869",
    appId: "1:577523729869:web:bd73dcb92ed702eef4f084"
  };

  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  //var db = firebase.firestore();

  let db = firebase.firestore();

  const SaveUser =(user)=>{

  db.collection("usuario").add({
      user
  })
      .then((docRef) => {
        MJSOK();
      })
      .catch((error) => {
        MJERROR();
  });
}

const MJSOK =()=>{
    Swal.fire(
        'Buen trabajo!',
        'Datos guardados correctamente!',
        'success'
      )
}

const MJERROR =()=>{
    Swal.fire(
        'ops!',
        'los datos no fueron guardados!',
        'error'
      )
}

$("#enviar").on('click',()=>{
  let usuario = $("#usuario");
  let email = $("#email");

  const user = {
    usuario,
    email
  } 
  SaveUser(user);
})



/*
const enviar = document.getElementById('enviar')

enviar.addEventListener('click', (e) => {
    e.preventDefault();
    const usuario = document.getElementById('usuario'),
          email = document.getElementById('email')
    
    const user = {
        usuario,
        email
    }

    SaveUser(user);

})*/
