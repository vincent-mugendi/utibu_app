import '/flutter_flow/flutter_flow_util.dart';
import 'sign_up_screen_widget.dart' show SignUpScreenWidget;
import 'package:flutter/material.dart';

class SignUpScreenModel extends FlutterFlowModel<SignUpScreenWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  final formKey = GlobalKey<FormState>();
  // State field(s) for Emailinput widget.
  FocusNode? emailinputFocusNode;
  TextEditingController? emailinputController;
  String? Function(BuildContext, String?)? emailinputControllerValidator;
  // State field(s) for Passwordinput widget.
  FocusNode? passwordinputFocusNode1;
  TextEditingController? passwordinputController1;
  String? Function(BuildContext, String?)? passwordinputController1Validator;
  // State field(s) for Passwordinput widget.
  FocusNode? passwordinputFocusNode2;
  TextEditingController? passwordinputController2;
  String? Function(BuildContext, String?)? passwordinputController2Validator;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
    emailinputFocusNode?.dispose();
    emailinputController?.dispose();

    passwordinputFocusNode1?.dispose();
    passwordinputController1?.dispose();

    passwordinputFocusNode2?.dispose();
    passwordinputController2?.dispose();
  }
}
