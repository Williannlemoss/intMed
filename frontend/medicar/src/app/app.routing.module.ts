import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {HomeComponent} from './components/home/home.component';
import {LoginComponent} from './components/login/login.component';
import {RegistroComponent} from './components/registro/registro.component';

const routes: Routes = [
  { path: 'consulta', component: HomeComponent},
  { path: 'login', component: LoginComponent},
  { path: 'registro', component: RegistroComponent}
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule {}
