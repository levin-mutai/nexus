import { Component, OnInit } from '@angular/core';
import { ShopService } from '../services/shops/shop.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-shop',
  templateUrl: './shop.component.html',
  styleUrls: ['./shop.component.scss'],
})
export class ShopComponent implements OnInit {
  all_shops: any[] = [];
  constructor(private shops: ShopService, private router: Router) {}

  ngOnInit() {
    this.shops.getShops().subscribe((response) => {
      this.all_shops = response;
      console.log(this.all_shops);
    });
  }

  onCardClick(shopid: string) {
    console.log('clicked');
    this.router.navigate(['/shops/' + shopid]);
  }
}
