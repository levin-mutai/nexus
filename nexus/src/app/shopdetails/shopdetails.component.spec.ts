import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShopdetailsComponent } from './shopdetails.component';
import { Shop } from '../models/shop.models';

describe('ShopdetailsComponent', () => {
  let component: ShopdetailsComponent;
  let fixture: ComponentFixture<ShopdetailsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ShopdetailsComponent],
    });
    fixture = TestBed.createComponent(ShopdetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
