import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MulkListesi } from './mulk-listesi';

describe('MulkListesi', () => {
  let component: MulkListesi;
  let fixture: ComponentFixture<MulkListesi>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MulkListesi]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MulkListesi);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
