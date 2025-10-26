import { TestBed } from '@angular/core/testing';

import { Portfoy } from './portfoy';

describe('Portfoy', () => {
  let service: Portfoy;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Portfoy);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
