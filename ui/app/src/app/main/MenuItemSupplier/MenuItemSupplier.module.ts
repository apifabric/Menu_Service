import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {MENUITEMSUPPLIER_MODULE_DECLARATIONS, MenuItemSupplierRoutingModule} from  './MenuItemSupplier-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    MenuItemSupplierRoutingModule
  ],
  declarations: MENUITEMSUPPLIER_MODULE_DECLARATIONS,
  exports: MENUITEMSUPPLIER_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class MenuItemSupplierModule { }