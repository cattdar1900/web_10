import { Component, OnInit } from '@angular/core';
import { RegisterServiceService } from './register-service.service';
import { Response } from 'selenium-webdriver/http';

@Component({
  selector: 'app-register-page',
  templateUrl: './register-page.component.html',
  styleUrls: ['./register-page.component.css'],
  providers : [RegisterServiceService]
})
export class RegisterPageComponent implements OnInit {

  constructor(private registerServiceService:RegisterServiceService) { }
  registers;

  ngOnInit() {
    this.registers = {
      name: '',
      major: '',
      studentID: '',
      userName: '',
      userPass: ''
    };
  }

  registerUser() {
    this.registerServiceService.registerNewUser(this.registers).subscribe(
      response => {
        alert('User' + this.registers.userName + 'complated !')
      },
      error => console.log('error',error)
    );
      
  }

}
