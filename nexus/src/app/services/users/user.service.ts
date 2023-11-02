import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor() {}

  login() {
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
