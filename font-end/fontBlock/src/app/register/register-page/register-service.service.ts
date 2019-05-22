import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RegisterServiceService {

  constructor(private http : HttpClient) {

  }

  registerNewUser(userData): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/Student',userData);
  }

}
