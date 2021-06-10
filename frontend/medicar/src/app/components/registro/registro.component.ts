import { Component } from '@angular/core';

@Component({
  selector: 'medicar-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent {

  criarUsuario() {
    window.location.assign('/login');
  }
}
