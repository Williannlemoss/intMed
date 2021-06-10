import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'medicar-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  user = 'willian';
  constructor() { }

  ngOnInit() {
  }

}
