import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginPageComponent} from './login/login-page/login-page.component'
import { RegisterPageComponent } from './register/register-page/register-page.component';
import { ShowWorkComponent } from './show-work/show-work.component';


const routes: Routes = [
  {path:'',component:LoginPageComponent},
  {path:'check',component:RegisterPageComponent},
  {path:'show',component:ShowWorkComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
