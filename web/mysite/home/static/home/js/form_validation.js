document.getElementById('registration-form').addEventListener('submit', function (event) {
    const password1 = document.getElementById('password1');
    const password2 = document.getElementById('password2');

    console.log("The password is : " + password1.value)
    console.log("The confirmation password is : " + password2.value)
    console.log("The lenght of the password is : " + password1.value.length)


    if (password1.value.length < 8){
      event.preventDefault();
      password1.classList.add('is-invalid');
      document.querySelector('"password1 + .invalid-feedback').textContent = 'Password is too short.'
    }

    if (password1.value !== password2.value) {
      event.preventDefault(); // Prevent form submission
      password2.classList.add('is-invalid');
      document.querySelector('#password2 + .invalid-feedback').textContent = 'Passwords do not match.';
    } else {
      password2.classList.remove('is-invalid');
    }

    // Add Bootstrap's was-validated class to show validation feedback
    if (!this.checkValidity()) {
      event.preventDefault();
      event.stopPropagation();
    }
    this.classList.add('was-validated');
  });

