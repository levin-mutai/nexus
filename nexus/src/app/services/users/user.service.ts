import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environment/environment';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(private http: HttpClient) {}
  headers = new HttpHeaders({
    'Content-Type': 'application/json',
  });
  login(data: {}) {
    this.http
      .post(environment.baseUrl + 'users/login', data, {
        headers: this.headers,
      })
      .subscribe((response) => {
        console.log(response);
      });
    localStorage.setItem('token', '123');
    localStorage.setItem('refreshToken', '123');
    localStorage.setItem('expiresAt', '123');
    localStorage.setItem('userId', '123');
    return true;
  }

  logout() {
    localStorage.removeItem('token');
  }

  refreshToken() {
    if (!localStorage.getItem('token')) return false;

    return true;
  }
  isLoggedIn() {
    return !!localStorage.getItem('token');
    // return !!localStorage.getItem('token') && this.refreshToken();
  }
}
