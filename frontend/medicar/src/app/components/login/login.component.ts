import { Component } from '@angular/core';

@Component({
  selector: 'medicar-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  logar() {
    window.location.assign('/consulta');
  }
}
