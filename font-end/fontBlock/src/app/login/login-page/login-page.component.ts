import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  data:any={}
  constructor(private router:Router) { }

  ngOnInit() {
    
  }
  SubmitdData(){
   console.log(this.data)
   this.router.navigate(['show',""])
}

}
