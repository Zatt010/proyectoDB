var hasChanges = false; // Variable para rastrear si ha habido cambios

function changeProfileImage() {
    var input = document.getElementById('profile-img-input');
    var image = document.getElementById('profile-img');
    var cancelButton = document.getElementById('cancel-profile-img');
    var updateButton = document.getElementById('update-profile-img');
  
    input.addEventListener('change', function(e) {
      var file = e.target.files[0];
      var reader = new FileReader();
  
      reader.onload = function(e) {
        image.src = e.target.result;
      }
  
      reader.readAsDataURL(file);
  
      image.classList.add('show');
      cancelButton.classList.add('show');
      updateButton.classList.add('show');
    });
  
    cancelButton.addEventListener('click', function() {
      input.value = '';
      image.src = 'ruta_de_la_imagen';
      image.classList.remove('show');
      cancelButton.classList.remove('show');
      updateButton.classList.remove('show');
    });
  
    updateButton.addEventListener('click', function() {
      // Lógica para actualizar la imagen en el servidor
      // ...
  
      // Resetear los elementos después de la actualización
      input.value = '';
      image.classList.remove('show');
      cancelButton.classList.remove('show');
      updateButton.classList.remove('show');
    });
  
    input.click();
    hasChanges = true;
}
  
function changeName() {
    var nameInput = document.createElement('input');
    nameInput.type = 'text';
    nameInput.id = 'name-input';
    nameInput.value = document.getElementById('name').textContent;
    nameInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            document.getElementById('name').textContent = nameInput.value;
            nameInput.parentNode.replaceChild(document.getElementById('name'), nameInput);
        }
    });

    document.getElementById('name').parentNode.replaceChild(nameInput, document.getElementById('name'));
    nameInput.focus();
    hasChanges = true;
}

function changeUsername() {
    var usernameInput = document.createElement('input');
    usernameInput.type = 'text';
    usernameInput.id = 'username-input';
    usernameInput.value = document.getElementById('username').textContent;
    usernameInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            document.getElementById('username').textContent = usernameInput.value;
            usernameInput.parentNode.replaceChild(document.getElementById('username'), usernameInput);
        }
    });

    document.getElementById('username').parentNode.replaceChild(usernameInput, document.getElementById('username'));
    usernameInput.focus();
    hasChanges = true;
}

function changeBirthdate() {
    var birthdateInput = document.createElement('input');
    birthdateInput.type = 'text';
    birthdateInput.id = 'birthdate-input';
    birthdateInput.value = document.getElementById('birthdate').textContent;
    birthdateInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            document.getElementById('birthdate').textContent = birthdateInput.value;
            birthdateInput.parentNode.replaceChild(document.getElementById('birthdate'), birthdateInput);
        }
    });

    // Eliminar cualquier instancia anterior del datepicker
    $('.datepicker').datepicker('remove');

    birthdateInput.classList.add('datepicker');
    birthdateInput.setAttribute('data-date-format', 'yyyy-mm-dd');

    birthdateInput.addEventListener('change', function() {
        document.getElementById('birthdate').textContent = birthdateInput.value;
        birthdateInput.parentNode.replaceChild(document.getElementById('birthdate'), birthdateInput);
    });

    birthdateInput.focus();

    document.getElementById('birthdate').parentNode.replaceChild(birthdateInput, document.getElementById('birthdate'));

    $('.datepicker').datepicker({
        language: 'es',
        autoclose: true
    }).datepicker('show');
    hasChanges = true;
}


function changeCountry() {
    var countryInput = document.createElement('input');
    countryInput.type = 'text';
    countryInput.id = 'country-input';
    countryInput.value = document.getElementById('country').textContent;
    countryInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            document.getElementById('country').textContent = countryInput.value;
            countryInput.parentNode.replaceChild(document.getElementById('country'), countryInput);
        }
    });

    document.getElementById('country').parentNode.replaceChild(countryInput, document.getElementById('country'));
    countryInput.focus();
    hasChanges = true;
}

function changeCi() {
    var ciInput = document.createElement('input');
    ciInput.type = 'text';
    ciInput.id = 'ci-input';
    ciInput.value = document.getElementById('ci').textContent;
    ciInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            document.getElementById('ci').textContent = ciInput.value;
            ciInput.parentNode.replaceChild(document.getElementById('ci'), ciInput);
        }
    });

    document.getElementById('ci').parentNode.replaceChild(ciInput, document.getElementById('ci'));
    ciInput.focus();
    hasChanges = true;
}

function changeEmail() {
    var emailInput = document.createElement('input');
    emailInput.type = 'text';
    emailInput.id = 'email-input';
    emailInput.value = document.getElementById('email').textContent;
    emailInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            document.getElementById('email').textContent = emailInput.value;
            emailInput.parentNode.replaceChild(document.getElementById('email'), emailInput);
        }
    });

    document.getElementById('email').parentNode.replaceChild(emailInput, document.getElementById('email'));
    emailInput.focus();
    hasChanges = true;
}

document.addEventListener('input', function() {
    var updateButton = document.getElementById('update-profile-img');
  
    if (hasChanges) {
        updateButton.style.display = 'block';
    } else {
        updateButton.style.display = 'none';
    }
});
