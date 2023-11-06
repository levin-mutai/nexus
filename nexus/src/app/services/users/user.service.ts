import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environment/environment';
import { Router } from '@angular/router';

interface MyResponse {
  status: number;
}

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(private http: HttpClient, private router: Router) {}
  headers = new HttpHeaders({
    'Content-Type': 'application/json',
  });
  login(data: {}) {
    this.http
      .post<MyResponse>(environment.baseUrl + '/user/login', data, {
        headers: this.headers,
      })
      .subscribe((response) => {
        if ('access' in response) {
          // Access the access token
          let accessToken: string = response['access'] as string;

          console.log(response.status);

          localStorage.setItem('token', accessToken);
          this.router.navigate(['/shops']);
        } else {
          console.error('Access Token not found in the response');
        }

        console.log(response);
      });

    return true;
  }

  register(data: {}) {
    this.http
      .post(environment.baseUrl + '/user/register', data, {
        headers: this.headers,
      })
      .subscribe((response) => {
        if ('email' in response) {
          console.log(response);

          this.router.navigate(['/login']);
        }
      });
  }

  logout() {
    localStorage.removeItem('token');
  }

  isLoggedIn() {
    return !!localStorage.getItem('token');
  }
}
