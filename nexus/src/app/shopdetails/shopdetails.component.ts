import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ShopService } from '../services/shops/shop.service';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-shopdetails',
  templateUrl: './shopdetails.component.html',
  styleUrls: ['./shopdetails.component.scss'],
})
export class ShopdetailsComponent implements OnInit {
  shop_details: any;
  ngOnInit(): void {
    this.shop.getShops(this.shopId).subscribe((response) => {
      console.log(response);
      this.shop_details = response;
    });
  }
  shopId!: string;
  products!: any;

  productDetails(): any {
    this.shop.getProducts().subscribe((response) => {
      console.log(response);
      this.products = response;
    });
    return this.products;
  }

  constructor(private route: ActivatedRoute, private shop: ShopService) {
    this.route.params.subscribe((params) => {
      this.shopId = params['id'];
    });
  }
}
