import '/flutter_flow/flutter_flow_util.dart';
import 'login_screen_widget.dart' show LoginScreenWidget;
import 'package:flutter/material.dart';

class LoginScreenModel extends FlutterFlowModel<LoginScreenWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  final formKey = GlobalKey<FormState>();
  // State field(s) for Emailinput widget.
  FocusNode? emailinputFocusNode;
  TextEditingController? emailinputController;
  String? Function(BuildContext, String?)? emailinputControllerValidator;
  // State field(s) for Passwordinput widget.
  FocusNode? passwordinputFocusNode;
  TextEditingController? passwordinputController;
  String? Function(BuildContext, String?)? passwordinputControllerValidator;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
    emailinputFocusNode?.dispose();
    emailinputController?.dispose();

    passwordinputFocusNode?.dispose();
    passwordinputController?.dispose();
  }
}
