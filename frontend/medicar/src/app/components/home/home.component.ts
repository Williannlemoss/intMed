import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'medicar-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  user = 'willian';
  constructor() { }

  ngOnInit() {
  }

}
