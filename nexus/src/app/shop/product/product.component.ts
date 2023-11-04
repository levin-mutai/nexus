import { Component, Input } from '@angular/core';
import { ShopService } from 'src/app/services/shops/shop.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss'],
})
export class ProductComponent {
  @Input()
  productData!: any;

  displayedColumns: string[] = ['property', 'value'];

  constructor(private shop: ShopService) {
    this.shop.getProducts().subscribe((data) => {
      this.productData = data;
    });
  }
}
