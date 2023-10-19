import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FitComponentComponent } from './fit-component.component';

describe('FitComponentComponent', () => {
  let component: FitComponentComponent;
  let fixture: ComponentFixture<FitComponentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [FitComponentComponent]
    });
    fixture = TestBed.createComponent(FitComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
