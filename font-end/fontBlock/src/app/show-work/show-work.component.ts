import { Component, OnInit } from '@angular/core';




@Component({
  selector: 'app-show-work',
  templateUrl: './show-work.component.html',
  styleUrls: ['./show-work.component.css']
})
export class ShowWorkComponent implements OnInit {
  
  BASE_URL = "http://127.0.0.1:8000/";
  

  constructor() { }
  registers;

  ngOnInit() {
    this.registers = {
      fullname:'',
      studentID:'',
      major:'',
      userName:'',
      passWord:''
    };
  }

}
