import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ShowserviceService {
  endpoint = "http://127.0.0.1:8000/Student";
  constructor(private http: HttpClient) { }
  

  getConfig() {
    // now returns an Observable of Config
    
    
  }
}
