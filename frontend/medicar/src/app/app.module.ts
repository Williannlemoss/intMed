import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import { AppComponent } from './app.component';
import {HomeModule} from './components/home/home.module';
import {AppRoutingModule} from './app.routing.module';
import {LoginModule} from './components/login/login.module';
import {RegistroModule} from './components/registro/registro.module';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    HomeModule,
    AppRoutingModule,
    LoginModule,
    RegistroModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
