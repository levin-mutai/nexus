import { Component, Input } from '@angular/core';
import { ShopService } from 'src/app/services/shops/shop.service';
import { ProductCreateComponent } from '../product-create/product-create.component';
import { MatDialog } from '@angular/material/dialog';
import { UserService } from 'src/app/services/users/user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss'],
})
export class ProductComponent {
  @Input()
  productData!: any;

  displayedColumns: string[] = ['property', 'value'];

  constructor(
    private shop: ShopService,
    public dialog: MatDialog,
    private user: UserService,
    private router: Router
  ) {
    this.shop.getProducts().subscribe((data) => {
      this.productData = data;
    });
  }

  openDialog() {
    if (!this.user.isLoggedIn()) {
      this.router.navigate(['/login']);
    } else {
      const dialogRef = this.dialog.open(ProductCreateComponent, {
        height: '560px',
        width: '600px',
      });

      dialogRef.afterClosed().subscribe((result) => {
        console.log(`Dialog result: ${result}`);
      });
    }
  }
}
