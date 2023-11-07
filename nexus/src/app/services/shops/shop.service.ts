import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { environment } from 'src/environment/environment';
import { UserService } from '../users/user.service';
import { Observable } from 'rxjs';
import { Product, Shop, ShopCreate } from 'src/app/models/shop.models';

@Injectable({
  providedIn: 'root',
})
export class ShopService {
  constructor(
    private http: HttpClient,
    private router: Router,
    private user: UserService
  ) {}
  token = localStorage.getItem('token');
  logedin: boolean = this.user.isLoggedIn();

  headers = new HttpHeaders({
    'Content-Type': 'application/json',
    Authorization: `Bearer ${this.token}`,
  });

  getShops(shop_id = ''): Observable<any> {
    if (shop_id == '') {
      return this.http.get(environment.baseUrl + '/shops', {
        headers: this.headers,
      });
    } else {
      return this.http.get(environment.baseUrl + '/shops/' + shop_id, {
        headers: this.headers,
      });
    }
  }

  createShop(shop: ShopCreate) {
    return this.http.post(environment.baseUrl + '/shops', shop, {
      headers: this.headers,
    });
  }

  createProducts(product: Product) {
    return this.http.post(environment.baseUrl + '/shops/products', product, {
      headers: this.headers,
    });
  }

  getProducts(product_id = ''): Observable<any> {
    if (product_id == '') {
      return this.http.get(environment.baseUrl + '/shops/products', {
        headers: this.headers,
      });
    } else {
      return this.http.get(
        environment.baseUrl + '/shops/products/' + product_id,
        {
          headers: this.headers,
        }
      );
    }
  }
}
