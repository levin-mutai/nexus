import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { shopsGuard } from './shops.guard';

describe('shopsGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) => 
      TestBed.runInInjectionContext(() => shopsGuard(...guardParameters));

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
