import {NgModule} from '@angular/core';
import {HeaderComponent} from './header/header.component';
import {HomeComponent} from './home.component';
import { TableComponent } from './table/table.component';
import {CommonModule} from '@angular/common';

@NgModule({
  declarations: [
    HomeComponent,
    HeaderComponent,
    TableComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    HomeComponent
  ]
})
export class HomeModule { }
